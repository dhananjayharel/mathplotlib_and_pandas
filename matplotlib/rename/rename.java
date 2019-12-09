// Java program to illustrate 
// how to rename Multiple Files 
// together using single program 
import java.io.*; 
import java.io.IOException; 

public class rename 
{ 
	public static void main(String[] argv) throws IOException 
	{ 
		// Path of folder where files are located 
		String folder_path = 
			"./"; 
		String folder_path2 = 
			"E:\\teachable-krazykoder\\Source Code\\changed"; 


	String configContents = "{\"giturl\":\"https://github.com/dhananjayharel/mathplotlib_and_pandas\",\r\n"+
"\"projectpath\":\"/home/project/mathplotlib_and_pandas/matplotlib/PLACEHOLDER\",\r\n"+
"\"projectname\":\"PLACEHOLDER\",\r\n"+
"\"setdynamicpath\":true,\r\n"+
"\"reloadwindow\":true,\r\n"+
"\"showLeftPanel\":false,\r\n"+
"\"showRightPanel\":false,\r\n"+
"\"showOutline\":false\r\n"+
"}\r\n";

String pmainFileContent = "{\"mainfile\":\"PLACEHOLDER2\",\r\n"+
"\"compilemenucommand\":\"python3 PLACEHOLDER2\",\r\n"+
"\"runmenucommand\":\"python3 PLACEHOLDER2\"\r\n"+
"}";
	

		// creating new folder 
		File myfolder = new File(folder_path); 

		File[] file_array = myfolder.listFiles(); 
		for (int i = 0; i < file_array.length; i++) 
		{ 

			if (file_array[i].isFile()) 
			{ 

				File myfile = new File(folder_path + 
						"\\" + file_array[i].getName()); 
				String long_file_name = file_array[i].getName(); 
				
				String[] tokens = long_file_name.split("\\s"); 
				String new_file_name = long_file_name.replaceAll("^\\d+ - ","");
			new_file_name = new_file_name.replaceAll(" ","_"); 
			new_file_name = new_file_name.replaceAll(",","");	
			String dirName = new_file_name.substring(0,new_file_name.indexOf("."));
              File projectDir = new File(dirName);
              boolean bool = projectDir.mkdir();			
				//System.out.println(long_file_name); 
				System.out.println("|"+new_file_name+"|"); 
				
			//write .configfile
			System.out.println(projectDir.getAbsolutePath());
			System.out.println(projectDir.getPath());
             File configFile = new File(projectDir.getAbsolutePath()+"/.configfile");
				configFile.createNewFile();
			FileWriter writer = new FileWriter(configFile);
			String configTest = configContents.replaceAll("PLACEHOLDER",dirName);
			writer.write(configTest);
			writer.close();	

            //write pmainfile
             File pmainFile = new File(projectDir.getAbsolutePath()+"/.pmainfile");
				pmainFile.createNewFile();
			FileWriter writer2 = new FileWriter(pmainFile);
			String pmainFileText = pmainFileContent.replaceAll("PLACEHOLDER2",new_file_name);
			writer2.write(pmainFileText);
			writer2.close();	 			
			
				// file name format: "Snapshot 11 (12-05-2017 11-57).png" 
				// To Shorten it to "11.png", get the substring which 
				// starts after the first space character in the long 
				// _file_name. 
				myfile.renameTo(new File(folder_path + "\\" +dirName+"\\"+ new_file_name)); 
			} 
		} 
	} 
} 
