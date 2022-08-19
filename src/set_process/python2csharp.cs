namespace Namespace {
    
    using system = os.system;
    
    using chdir = os.chdir;
    
    public static class Module {
        
        public static object src = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/";
        
        public static object filename = "lfb.py";
        
        public static object argument0 = "";
        
        public static object argument1 = "routine_execution";
        
        static Module() {
            system("cls");
            chdir(src);
            system("python " + filename + " " + argument0);
        }
    }
}
