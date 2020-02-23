import clr
clr.AddReference('System.Windows.Forms')
clr.AddReference('IronPython.Wpf')

#Speicherort von xaml-Datei
from pyrevit import script
xamlfile = script.get_bundle_file('ui.xaml')

#Hauptfenster für den WPF Creator
import wpf
from System import Windows

class MyWindow(Windows.Window):
    def __init__(self):
        wpf.LoadComponent(self, xamlfile)


#Fenster anzeigen lassen
 MyWindow().ShowDialog()