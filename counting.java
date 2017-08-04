import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class counting {
    public static void main (String[] args) {
        //Get the input string
        Scanner in = new Scanner(System.in);
        System.out.print("Enter your string:\n>>> ");
        String inputString = in.nextLine();

        //HashMap
        HashMap<Character, Integer> compareList = new HashMap<>();

        //Put char(c) in HashMap, count
        for (char c : inputString.toCharArray()){
            if (!compareList.containsKey(c)) {
                compareList.put(c, 1);
            } else {
                compareList.put(c, compareList.get(c) + 1);
            }
        }
        System.out.println(compareList);
        //String table = "";
        for (Map.Entry<Character, Integer> value : compareList.entrySet()){
            String table =((value.getKey().toString() + ":\t" + value.getValue().toString()));
            System.out.println(table);
        }

    }
}