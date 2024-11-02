import java.io.File;import java.util.ArrayList;import java.util.Collections;import java.util.Scanner;public class CountWords {    public static void main(String[] args) throws Exception {        // Create a Scanner object to read from the text file        File file = new File("text.txt");        Scanner inputScanner = new Scanner(file);        // Create an ArrayList to store WordOccurrence objects        ArrayList<WordOccurrence> wordOccurrences = new ArrayList<WordOccurrence>();        // Read words from the file and count their occurrences        while (inputScanner.hasNext()) {            String word = inputScanner.next().toLowerCase();            // Remove punctuation marks (imperfection here, we don't handle all punctuation)            word = word.replaceAll("[.,!?()]", "");            // Check if the word is already in the list of wordOccurrences            boolean found = false;            for (WordOccurrence wordOccurrence : wordOccurrences) {                if (wordOccurrence.getWord().equals(word)) {                    wordOccurrence.incrementCount();                    found = true;                    break;                }            }            // If the word is not found, add it to the list            if (!found) {                wordOccurrences.add(new WordOccurrence(word, 1));            }        }        // Sort the wordOccurrences list in ascending order of occurrence counts        Collections.sort(wordOccurrences);        // Display the words and their occurrence counts        for (WordOccurrence wordOccurrence : wordOccurrences) {            System.out.println(wordOccurrence.getWord() + ": " + wordOccurrence.getCount());        }        // Close the scanner        inputScanner.close();    }}class WordOccurrence implements Comparable<WordOccurrence> {    private String word;    private int count;    public WordOccurrence(String word, int count) {        this.word = word;        this.count = count;    }    public String getWord() {        return word;    }    public int getCount() {        return count;    }    public void incrementCount() {        count++;    }    @Override    public int compareTo(WordOccurrence other) {        // Compare WordOccurrence objects based on occurrence counts        return Integer.compare(this.count, other.count);    }}