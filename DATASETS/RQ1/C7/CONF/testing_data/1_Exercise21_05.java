



public class nan{
    private static final String KEYWORD = "keyword_style_class";
    private static final String COMMENT = "comment_style_class";
    private static final String LITERAL = "literals_style_class";

    private static final String CSS_STYLE = "div{display: inline-block}" +
            ".none{font-weight: normal;color:black;}" +
            " .keyword_style_class {font-weight: bold;color: navy;}" +
            " .comment_style_class {font-weight: bold; color: green;}" +
            " .literals_style_class {font-weight: bold; color: blue;}";

    private static final String[] KEY_WORDS = {"abstract", "assert", "boolean",
            "break", "byte", "case", "catch", "char", "class", "const",
            "continue", "default", "do", "double", "else", "enum",
            "extends", "for", "final", "finally", "float", "goto",
            "if", "implements", "import", "instanceof", "int",
            "interface", "long", "native", "new", "package", "private",
            "protected", "public", "return", "short", "static",
            "strictfp", "super", "switch", "synchronized", "this",
            "throw", "throws", "transient", "try", "void", "volatile",
            "while", "true", "false", "null"};

    public static void main(String[] args) {
        if (args.length < 2) {
            System.out.println("Usage: java nanWelcome.java Welcome.html");
            System.exit(1);
        }

        String inputFile = args[0];
        String outputFile = args[1];
        System.out.println("Reading file: " + inputFile);

        try {
            List<String> txtLines = Files.readAllLines(Paths.get(inputFile));
            System.out.println("Reading complete.\nMapping input file to HTML file...");

            ArrayList<String> htmlFileLines = mapTextToHtml(txtLines);

            System.out.println("Mapping complete...");
            System.out.println("Writing output file: " + outputFile);

            Files.write(Paths.get(outputFile), htmlFileLines, StandardOpenOption.CREATE);
            System.out.println("Writing output file complete.");

        } catch (IOException e) {
            System.out.println("Something went wrong during read/convert/write...");
            e.printStackTrace();
        }
    }

    private static ArrayList<String> mapTextToHtml(List<String> txtFileLines) {
        ArrayList<String> htmlLines = new ArrayList<>();
        htmlLines.add("<html lang=\"en\">");
        htmlLines.add("<head>");
        htmlLines.add("<style>");
        htmlLines.add(CSS_STYLE);
        htmlLines.add("</style>");
        htmlLines.add("<title>" + Exercise21_05.class.getName() + "</title>");
        htmlLines.add("</head>");
        htmlLines.add("<body>");

        Set<String> keywordSet = new HashSet<>(Arrays.asList(KEY_WORDS));
        
        for (String txtFileLine : txtFileLines) {
            StringBuilder lineBuilder = new StringBuilder();
            lineBuilder.append("<div>"); 
            String[] words = txtFileLine.split(" "); 
            
            for (int idx = 0; idx < words.length; idx++) {
                if (words[idx].startsWith("
                    lineBuilder.append("<div class=\"" + COMMENT + "\">"); 
                    while (idx < words.length) { 
                        lineBuilder.append(words[idx]).append("&nbsp;");
                        idx++;
                    }
                    lineBuilder.append("</div>"); 
                    continue;
                }

                if (keywordSet.contains(words[idx])) {
                    lineBuilder.append("<div class=\"" + KEYWORD + "\">"); 
                    lineBuilder.append(words[idx]).append("&nbsp;");
                    lineBuilder.append(" </div>"); 
                    continue;
                }

                if (words[idx].startsWith("\"")) {
                    lineBuilder.append("<div class=\"" + LITERAL + "\">"); 
                    while (!words[idx].endsWith("\"")) { 
                        lineBuilder.append(words[idx]).append("&nbsp;");
                        idx++;
                    }
                    lineBuilder.append(words[idx]).append("&nbsp;");
                    lineBuilder.append("</div>"); 
                    continue;
                }
                if (words[idx].isEmpty()) {
                    lineBuilder.append("&nbsp;");
                } else {
                    
                    lineBuilder.append(words[idx]).append("&nbsp;");
                }
            }
            htmlLines.add(lineBuilder + "</div><br>");
        }
        htmlLines.add("</body>");
        htmlLines.add("</html>");

        return htmlLines;
    }
}
