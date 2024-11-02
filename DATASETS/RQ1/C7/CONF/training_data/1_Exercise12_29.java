



public class NamePadder{
    private static final Pattern PATTERN = Pattern.compile("Exercise\\d{1,2}_\\d.*"); 

    public static void main(String[] args) {

        if (args.length < 1) {
            System.out.println("Usage: java NamePadder*");
            return;
        }
        if (!args[0].equals("*")) {
            System.out.println("Usage: java NamePadder*");
            return;
        }

        File srcDirectory = new File("./testDir");
        if (!srcDirectory.isDirectory()) {
            System.out.println("The directory path is not a directory: " + srcDirectory.getAbsolutePath());
            return;
        }

        if (!Objects.isNull(srcDirectory.listFiles()) && srcDirectory.listFiles().length > 0) {
            ArrayList<File> files = new ArrayList<>(Arrays.asList(srcDirectory.listFiles()));
            for (File f : files) {
                String fileName = f.getName();
                StringBuffer stringBuffer = new StringBuffer(fileName);
                if (PATTERN.matcher(stringBuffer.toString()).matches()) {
                    stringBuffer.insert(fileName.lastIndexOf("_") + 1, "0");
                    System.out.println("Renaming: " + fileName + " to " + stringBuffer.toString());
                    Path srcPath = f.toPath();
                    Path trgtPath = Paths.get(srcDirectory.toPath().toString(), stringBuffer.toString());
                    try {
                        Files.move(srcPath, trgtPath, StandardCopyOption.REPLACE_EXISTING);
                        System.out.println("Rename successful");
                    } catch (IOException ioe) {
                        System.out.println("Something went wrong while renaming the file... " + fileName + "\n\n");
                        ioe.printStackTrace();
                    }

                }

            }
        } else {
            System.out.println("The current directory is empty...");
        }

    }
}
