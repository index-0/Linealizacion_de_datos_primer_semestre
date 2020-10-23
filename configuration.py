#!/usr/bin/env python

########################
# Graphs customization #
########################

# Latex #
latex = True
unicode = True
# Font families = ['serif', 'sans-serif', 'cursive', 'monospace']
font_family = 'serif'
# Serif fonts = ['Times', 'Palatino', 'New Century Schoolbook', 'Bookman', 'Computer Modern Roman']
# Sans-serif fonts = ['Helvetica', 'Avant Garde', 'Computer Modern Sans serif']
# Cursive fonts = ['Zapf Chancery']
# Monospace fonts = ['Courier', 'Computer Modern Typewriter']
font = 'Computer Modern Roman'
font_size = 12
label_font_size = 12

# Scale factors #
line_width   = 1.2
marker_size  = 1.2
marker_width = 1.2

# Data graph #
data_graph_title = 'Data'                                    # Title of the label for the data graph.
data_graph_line_type = '-'                                   # [| '-' | '--' | '-.' | ':' | 'None' | ' ' | ''] (str)
data_graph_line_color = '#361156'                            # Hex color (str)
data_graph_line_width = 1.0 * line_width                     # (float)
data_graph_marker_type = '.'                                 # https://matplotlib.org/api/markers_api.html#module-matplotlib.markers (str)
data_graph_marker_color = '#361156'                          # Hex color (str)
data_graph_marker_size = 6.0 * marker_size                   # (float)
data_graph_marker_edge_color = '#000000'                     # Hex color (str)
data_graph_marker_edge_width = 0.5 * marker_width            # (float)
data_graph_transparency = 1.0                                # 0.0 transparent through 1.0 opaque (float)

# Equation graph #
equation_graph_line_type = '-'                               # [| '-' | '--' | '-.' | ':' | 'None' | ' ' | ''] (str)
equation_graph_line_color = '#287086'                        # Hex color (str)
equation_graph_line_width = 1.0                              # (float)
equation_graph_transparency = 1.0                            # 0.0 transparent through 1.0 opaque (float)

# Comparison graph #
comparison_graph_data_line_type = 'None'                     # [| '-' | '--' | '-.' | ':' | 'None' | ' ' | ''] (str)
comparison_graph_data_line_color = '#361156'                 # Hex color (str)
comparison_graph_data_lide_width = 1.0 * line_width          # (float)
comparison_graph_data_marker_type = '.'                      # https://matplotlib.org/api/markers_api.html#module-matplotlib.markers (str)
comparison_graph_data_marker_color = '#361156'               # Hex color (str)
comparison_graph_data_marker_size = 6.0 * marker_size        # (float)
comparison_graph_data_marker_edge_color = '#361156'          # Hex color (str)
comparison_graph_data_marker_edge_width = 0.5 * marker_width # (float)
comparison_graph_data_transparency = 1.0                     # 0.0 transparent through 1.0 opaque (float)

comparison_graph_equation_line_type = '-'                    # [| '-' | '--' | '-.' | ':' | 'None' | ' ' | ''] (str)
comparison_graph_equation_line_color = '#287086'             # Hex color (str)
comparison_graph_equation_line_width = 1.0 * line_width      # (float)
comparison_graph_equation_transparency = 1.0                 # 0.0 transparent through 1.0 opaque (float)

# Save parameters #
save_format = 'png'                                          # One of the file extensions supported png, pdf, ps, eps or svg. (str)
save_dpi = 250                                               # The resolution in dots per inch. (int)
save_transparent = True                                      # (boolean)
save_bbox_inches = 'tight'                                   # Bbox in inches. Only the given portion of the figure is saved. If ‘tight’, try to figure out the tight bbox of the figure. (float) or (str) for 'tight'.
save_pad_inches = 0.1                                        # Amount of padding around the figure when bbox_inches is ‘tight’. (float)
save_orientation = 'portrait'                                # [ ‘landscape’ | ‘portrait’ ] (str)

antialiased = True                                           # Render lines in antialised (no jaggies) (boolean)

###################
# Terminal colors #
###################
C1 = "\33[32m"                                               # Output color
C2 = "\33[31m"                                               # Warning color
C3 = "\33[34m"                                               # Input color
CE = "\x1b[0m"

# To disable a color change the value to "". example: (C1 = "")

