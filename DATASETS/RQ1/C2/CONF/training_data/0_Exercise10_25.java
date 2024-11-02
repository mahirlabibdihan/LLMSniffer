public static String[] split(String s, String regex) {
    List<String> parts = new ArrayList<>();
    Pattern pattern = Pattern.compile(regex);
    Matcher matcher = pattern.matcher(s);
    int lastEnd = 0;
    while (matcher.find()) {
        String part = s.substring(lastEnd, matcher.end());
        parts.add(part);
        lastEnd = matcher.end();
    }
    if (lastEnd < s.length()) {
        String
