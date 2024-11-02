import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Random;

public class Hangman {
    public static void main(String[] args) {
        final int MAX_WRONG_GUESSES = 7;
        File file = new File("hangman.txt");
        Scanner input = null;
        try {
            input = new Scanner(file);
        } catch (FileNotFoundException e) {
            System.out.println("Could not find file: " + file);
            System.exit(1);
        }
        String[] words = input.nextLine().split("\\s+");
        input.close();
        Random random = new Random();
        String word = words[random.nextInt(words.length)];
        char[] hiddenWord = new char[word.length()];
        for (int i = 0; i < hiddenWord.length; i++) {
            hiddenWord[i] = '*';
        }
        int wrongGuesses = 0;
        Scanner keyboard = new Scanner(System.in);
        while (wrongGuesses < MAX_WRONG_GUESSES && new String(hiddenWord).contains("*")) {
            System.out.print("(Guess) Enter a letter in word " + new String(hiddenWord) + " > ");
            char guess = keyboard.nextLine().charAt(0);
            boolean correctGuess = false;
            for (int i = 0; i < word.length(); i++) {
                if (word.charAt(i) == guess && hiddenWord[i] == '*') {
                    hiddenWord[i] = guess;
                    correctGuess = true;
                }
            }
            if (!correctGuess) {
                System.out.println(guess + " is not in the word.");
                wrongGuesses++;
            }
        }
        keyboard.close();
        if (new String(hiddenWord).contains("*")) {
            System.out.println("You lose. The word was " + word);
        } else {
            System.out.println("Congratulations! You guessed the word: " + word);
        }
    }
}