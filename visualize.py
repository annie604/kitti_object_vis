import os
from mayavi import mlab

# Get the output directory from kitti_object.py or define it here
try:
    from kitti_object import OUTPUT_DIR
except ImportError:
    # Fallback if import fails
    OUTPUT_DIR = os.path.join(os.path.expanduser("~"), "kitti_output", "day-dgp")
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def visualize_point_cloud_with_boxes(point_cloud, boxes, data_idx=None):
    # ...existing code for visualizing point cloud and boxes...

    # Set the initial view angle (azimuth, elevation, distance, focalpoint)
    mlab.view(azimuth=180, elevation=70, distance=50, focalpoint=(0, 0, 0))

    # Save the figure if data_idx is provided
    if data_idx is not None:
        try:
            save_path = f"{OUTPUT_DIR}/{data_idx}_visualization.png"
            print(f"Saving visualization to {save_path}")
            mlab.savefig(save_path)
            print(f"Successfully saved visualization")
        except Exception as e:
            print(f"Failed to save visualization: {e}")

    # Show the visualization
    mlab.show()
