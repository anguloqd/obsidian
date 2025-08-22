```
let
    // Lire la cellule nommée "TestSpecId"
    namedRange = Excel.CurrentWorkbook(){[Name="TestSpecId"]}[Content],
    param = if Table.RowCount(namedRange) > 0 then Record.Field(namedRange{0}, "Column1") else error "La cellule TestSpecId est vide ou introuvable.",

    // Construire l'URL
    url = "https://lims.se.com/STARLIMS11.prod/RESTServices.REST_API.TestSpec_MetaData.lims?TestSpecId=" & param & "&Version=1",

    // Définir les en-têtes
    headers = [
        #"Content-Type" = "application/json",
        #"STARLIMSUser" = "API_FRANCE",
        #"STARLIMSPass" = "LIMS",
        #"Cookie" = "ASP.NET_SessionId=...; AWSALB=...; AWSALBCORS=..."
    ],

    // Appel API
    response = Web.Contents(url, [Headers=headers]),
    json = Json.Document(response),

    // Extraire les champs simples
    metadata = [
        Confidentiality = json[Confidentiality],
        Laboratory = json[Laboratory],
        Object_ID = json[Object_ID],
        Origin_Of_Need = json[Origin_Of_Need],
        ParentSpec_Id = json[ParentSpec_Id],
        Project_Or_Activity_Name = json[Project_Or_Activity_Name],
        TestCategory = json[TestCategory],
        TestSpec_ID = json[TestSpec_ID],
        Title = json[Title]
    ],
    metaTable = Record.ToTable(metadata),
    metaExpanded = Table.AddColumn(metaTable, "Type", each "Meta"),
    metaRenamed = Table.RenameColumns(metaExpanded, {{"Name", "Champ"}, {"Value", "Valeur"}}),

    // Samples
    samples = if Record.HasFields(json, "Samples") and List.Count(json[Samples]) > 0 then
        let
            s = Table.FromList(json[Samples], Splitter.SplitByNothing(), null, null, ExtraValues.Error),
            sExpanded = Table.ExpandRecordColumn(s, "Column1", {"DESCRIPTION", "FAMILY1", "FAMILY2", "FAMILY3", "OTHER_ID", "SAMPLEID"}),
            sUnpivot = Table.UnpivotOtherColumns(sExpanded, {"SAMPLEID"}, "Champ", "Valeur"),
            sWithType = Table.AddColumn(sUnpivot, "Type", each "Sample")
        in
            sWithType
    else
        Table.FromRows({}, {"Champ", "Valeur", "SAMPLEID", "Type"}),

    // Test Parameters
    parameters = if Record.HasFields(json, "Test_Parameters") and List.Count(json[Test_Parameters]) > 0 then
        let
            p = Table.FromList(json[Test_Parameters], Splitter.SplitByNothing(), null, null, ExtraValues.Error),
            pExpanded = Table.ExpandRecordColumn(p, "Column1", {"name", "value"}),
            pRenamed = Table.RenameColumns(pExpanded, {{"name", "Champ"}, {"value", "Valeur"}}),
            pWithType = Table.AddColumn(pRenamed, "Type", each "Test_Parameter")
        in
            pWithType
    else
        Table.FromRows({}, {"Champ", "Valeur", "Type"}),

    // Standards
    standards = if Record.HasFields(json, "Standards") and List.Count(json[Standards]) > 0 then
        let
            st = Table.FromList(json[Standards], Splitter.SplitByNothing(), null, null, ExtraValues.Error),
            stExpanded = Table.ExpandRecordColumn(st, "Column1", {"Clause", "Standard", "Type"}),
            stUnpivot = Table.UnpivotOtherColumns(stExpanded, {}, "Champ", "Valeur"),
            stWithType = Table.AddColumn(stUnpivot, "Type", each "Standard")
        in
            stWithType
    else
        Table.FromRows({}, {"Champ", "Valeur", "Type"}),

    // Equipments
    equipments = if Record.HasFields(json, "Equipments") and List.Count(json[Equipments]) > 0 then
        let
            e = Table.FromList(json[Equipments], Splitter.SplitByNothing(), null, null, ExtraValues.Error),
            eExpanded = Table.ExpandRecordColumn(e, "Column1", {"EQID","XEXTERNAL_ID"}),
            eUnpivot = Table.UnpivotOtherColumns(eExpanded, {}, "Champ", "Valeur"),
            eWithType = Table.AddColumn(eUnpivot, "Type", each "Equipment")
        in
            eWithType
    else
        Table.FromRows({}, {"Champ", "Valeur", "Type"}),

    // Testers
    testers = if Record.HasFields(json, "Testers") and List.Count(json[Testers]) > 0 then
        let
            t = Table.FromList(json[Testers], Splitter.SplitByNothing(), null, null, ExtraValues.Error),
            tExpanded = Table.ExpandRecordColumn(t, "Column1", {"Name","SESA_ID"}),
            tUnpivot = Table.UnpivotOtherColumns(tExpanded, {}, "Champ", "Valeur"),
            tWithType = Table.AddColumn(tUnpivot, "Type", each "Tester")
        in
            tWithType
    else
        Table.FromRows({}, {"Champ", "Valeur", "Type"}),

    // Fusionner toutes les tables
    allTables = Table.Combine({metaRenamed, samples, parameters, standards, equipments, testers})
in
    allTables
```