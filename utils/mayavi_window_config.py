import argparse
from mayavi import mlab

def configure_mayavi_window(size=None, dpi=None):
    """Configure Mayavi window size and DPI settings.
    
    Args:
        size (tuple): Window size as (width, height) in pixels
        dpi (int): DPI setting for the window
    """
    fig = mlab.gcf()
    
    if size is not None:
        width, height = size
        # 明確設置窗口大小
        fig.scene.set_size((width, height))
        
        # 嘗試通過修改 mlab 的視窗屬性確保大小設置
        try:
            fig.scene._vtk_control.resize(width, height)
        except:
            pass
            
        # 確保場景已更新
        fig.scene.render()
    
    if dpi is not None:
        # Attempt to set DPI - this might not work in all versions
        try:
            fig.scene._tool_bar.setIconSize(dpi)
        except:
            pass
    
    return fig

def add_window_args(parser):
    """Add window configuration arguments to an ArgumentParser."""
    parser.add_argument('--size', type=lambda s: tuple(map(int, s.split(','))), 
                      default=(1024, 768),
                      help='Window size in width,height format (e.g. 1024,768)')
    parser.add_argument('--dpi', type=int, default=None,
                      help='DPI setting for window')
    return parser

# Example usage in your main script:
"""
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser = add_window_args(parser)
    args = parser.parse_args()
    
    # Your visualization code here
    # ...
    
    # Configure window
    configure_mayavi_window(size=args.size, dpi=args.dpi)
    
    mlab.show()
"""
