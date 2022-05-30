import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class hmwrk1 {

    public static void main(String[] args) {

        int counter;
        counter = readLines("input.txt");

        System.out.printf("\n%d lines were processed.", counter);
    }

    public static int readLines(String fileName){

        int counter = 0;

        try {
            Scanner input = new Scanner(new File(fileName));

            while(input.hasNextLine()){

                String word = input.nextLine();

                System.out.printf(" %3d. %s\n", counter, word);

                counter++;
            }
        }

        catch (FileNotFoundException e) {
            System.err.println("Error with file.");
            System.err.println(e.getMessage());
            System.exit(1);

        }

        return counter;
    }
}