/*
   FIBONACCI SERIES
   https://www.codeeval.com/open_challenges/22/
*/

import java.io.*;
public class Main {
    public static int fib (int index)
    {
        if (index == 0)
        {
            return 0;
        }
        else if (index == 1)
        {
            return 1;
        }
        else
        {
            return fib(index-1) + fib(index - 2);
        }
    }
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
            // Process line of input Here
            int index = Integer.valueOf(line);
            System.out.println(fib(index));
        }
    }
}