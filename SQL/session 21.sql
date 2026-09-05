-- task 1
--Connect an Excel workbook to a SQL Server database using Power Query and load the 'Restaurants' table (assume it contains columns like name, cuisine, rating) into a new worksheet.
let
    Source = Sql.Database("YOUR_SERVER", "YOUR_DATABASE"),
    Restaurants = Source{[Schema="dbo", Item="Restaurants"]}[Data],
    FilteredRestaurants = Table.SelectRows(
        Restaurants,
        each [cuisine] = Excel.CurrentWorkbook(){[Name="CuisineParameter"]}[Content]{0}[Column1]
    )
in
    FilteredRestaurants
    