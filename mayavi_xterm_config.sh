#!/bin/bash

# Set environment variables for better display handling in xterm
export QT_AUTO_SCREEN_SCALE_FACTOR=0
export QT_SCALE_FACTOR=1
export ETS_TOOLKIT=qt4
export MPLBACKEND="Qt5Agg"

# Instructions for use
echo "Mayavi xterm display configuration loaded."
echo "To use this configuration with normalized window sizes, run:"
echo "python kitti_object.py --show_lidar_with_depth --size 1024,768 [其他參數]"
echo "All Mayavi windows will use the specified window size."
