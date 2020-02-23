from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction,

uidoc = revit.ActiveUIDocument
doc = revit.ActiveUIDocument.Document

all_eq = DB.FilteredElementCollector(doc) \
           .OfCategory(DB.BuiltInCategory.OST_MechanicalEquipment) \
           .WhereElementIsNotElementType() \
           .ToElements()

t = Transaction(doc, "Transaction Name")
t.Start()

for eq in all_eq:
    t_mark = eq.LookupParameter('Breite')
    t_mark.Set('300')
    print(eq.Name)
    print(eq.Name, t_mark.AsString())
t.Commit()