import java.util.Random;

public class DiceRoller {

  public static void main(String[] args) {
    Random generator = new Random();
    int d = 0;

    while (d < 4) {
      System.out.print("Rolling... ");
      int face = 1 + generator.nextInt(6);
      System.out.print("I got a "+ face
        + ".  ");
      if (face == 1) {
        System.out.print("Wow! An ACE!");
      }
      System.out.println();
      d = d + 1;
    }
  }

}
