import geopandas as gpd
import numpy as np
from scipy.spatial import cKDTree
from shapely.geometry import Point
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

def calculate_boundary_distance(ringforts, territories):
    """
    Calculate the minimum distance from each ringfort to the nearest territory boundary.
    
    Args:
        ringforts (GeoDataFrame): GeoDataFrame containing ringfort locations
        territories (GeoDataFrame): GeoDataFrame containing territory boundaries
        
    Returns:
        Series: Minimum distances from each ringfort to the nearest territory boundary
    """
    # Get the boundary of all territories
    territory_boundaries = territories.geometry.boundary.unary_union
    
    # Calculate distance from each ringfort to the boundary
    distances = ringforts.geometry.apply(
        lambda x: territory_boundaries.distance(x)
    )
    
    return distances

def calculate_local_density(ringforts, radius=5000):
    """
    Calculate the local density of ringforts within a specified radius.
    
    Args:
        ringforts (GeoDataFrame): GeoDataFrame containing ringfort locations
        radius (float): Search radius in meters (default: 5000m)
        
    Returns:
        Series: Local density values for each ringfort
    """
    # Get coordinates of ringforts
    coords = np.array([(geom.x, geom.y) for geom in ringforts.geometry])
    
    # Create KDTree for efficient nearest neighbor search
    tree = cKDTree(coords)
    
    # Find all points within radius for each point
    counts = tree.query_ball_point(coords, radius, return_length=True)
    
    # Convert to density (points per square kilometer)
    area = np.pi * (radius/1000)**2  # Area in square kilometers
    densities = counts / area
    
    return densities

def visualize_results(model, feature_importance, y_test, y_pred, territories, X, ringforts):
    """
    Visualize the results of the ringfort analysis.
    
    Args:
        model: Trained RandomForest model
        feature_importance: DataFrame containing feature importance scores
        y_test: Test set labels
        y_pred: Predicted labels
        territories: GeoDataFrame containing territory boundaries
        X: Features DataFrame used for prediction
        ringforts: GeoDataFrame containing ringfort locations
        
    Returns:
        GeoDataFrame: Ringforts with predictions added as a new column
    """
    # Plot feature importance
    plt.figure(figsize=(12, 6))
    sns.barplot(x='importance', y='feature', data=feature_importance.head(10))
    plt.title('Top 10 Most Important Features for Ringfort Classification')
    plt.show()
    
    # Plot confusion matrix
    plt.figure(figsize=(8, 8))
    cm = confusion_matrix(y_test, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
    plt.title('Confusion Matrix of LISA Categories')
    plt.show()
    
    # Map predictions
    fig, ax = plt.subplots(figsize=(15, 15))
    territories.plot(ax=ax, alpha=0.5, edgecolor='black')
    
    # Exclude the target variable from features for prediction
    features_for_prediction = X.drop(columns=['lisa_category'], errors='ignore')
    
    # Get predictions for all ringforts
    predictions = model.predict(features_for_prediction)
    
    # Create a copy of ringforts with predictions
    ringforts_with_predictions = ringforts.copy()
    ringforts_with_predictions['predicted_category'] = predictions
    
    # Plot ringforts colored by predicted category
    scatter = ax.scatter(ringforts.geometry.x, ringforts.geometry.y,
                        c=predictions,
                        cmap='viridis',
                        s=100)
    plt.legend(scatter.legend_elements()[0], 
              ['HH', 'LH', 'LL', 'HL'],
              title='Predicted Categories')
    plt.title('Predicted Ringfort Categories')
    plt.show()
    
    return ringforts_with_predictions

def analyze_territorial_patterns(ringforts_with_predictions, territories):
    """
    Analyze the distribution of ringfort categories by territory.
    
    Args:
        ringforts_with_predictions: GeoDataFrame containing ringforts with predicted categories
        territories: GeoDataFrame containing territory boundaries
        
    Returns:
        DataFrame: Territory patterns analysis
    """
    # Perform spatial join to get territory information for each ringfort
    ringforts_with_territories = gpd.sjoin(ringforts_with_predictions, territories, how='left', predicate='within')
    
    # Calculate proportion of each predicted category per territory
    territory_patterns = ringforts_with_territories.groupby('ENGLISH')['predicted_category'].value_counts(normalize=True).unstack()
    
    # Plot territorial differences
    plt.figure(figsize=(15, 8))
    territory_patterns.plot(kind='bar', stacked=True)
    plt.title('Distribution of Predicted Ringfort Categories by Territory')
    plt.xlabel('Territory')
    plt.ylabel('Proportion')
    plt.legend(title='Category')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
    
    # Calculate summary statistics
    print("\nTerritory Analysis Summary:")
    print("-" * 50)
    print(f"Total territories analyzed: {len(territory_patterns)}")
    print(f"Total ringforts analyzed: {len(ringforts_with_territories)}")
    print("\nAverage distribution of categories across territories:")
    print(territory_patterns.mean())
    
    return territory_patterns

