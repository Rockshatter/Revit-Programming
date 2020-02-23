from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory, Transaction, TransactionGroup

doc = __revit__.ActiveUIDocument.Document

sheets_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets) \
                                                .WhereElementIsNotElementType() \
                                                .ToElementIds()

wall_id_collector = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Walls) \
                                                 .WhereElementIsNotElementType() \
                                                 .ToElementIds()

tg = TransactionGroup(doc, "Update and Delete")
tg.Start()

t = Transaction(doc, "Update Sheet Parameters")
t.Start()

for sheet in sheets_collector:
        custom_param = sheet.LookupParameter('-Beispielparameter-')
        if custom_param:
            custom_param.Set("Example value")

t.Commit()

t = Transaction(doc, "Deleting All Walls")
t.Start()

for wall_id in wall_id_collector:
        doc.Delete(wall_id)

t.Commit()

tg.Assimilate()

