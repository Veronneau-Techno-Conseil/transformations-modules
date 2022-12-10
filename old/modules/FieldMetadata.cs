namespace CommunAxiom.Commons.Client.Contracts.Ingestion.Configuration
{

    public class FieldMetaData
    {
        //[].name
        public string FieldName { get; set; }
        // string, number, date, boolean
        public string FieldType { get; set; }
        public int? Index { get; set; }
    }

    public enum FieldType
    {
        Text = 1,
        Number = 2,
        Password = 3,
        Lookup = 4,
        File = 5,
        Date = 6,
        Boolean = 7
    }

}