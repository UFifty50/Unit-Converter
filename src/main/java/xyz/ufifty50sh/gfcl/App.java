package xyz.ufifty50sh.gfcl;

import javax.swing.*;
import java.awt.*;

public class App extends JPanel {
    private static JFrame frame;
    private static JButton ctf;
    private static JButton ftc;
    private static JButton lyd;
    private static Container container;

    public static void main(String[] args) {
        frame = new JFrame("MyPanel");
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        container = frame.getContentPane();
        initWindow();
        setupListeners();
    }

    static void initWindow() {
        container.add(new App());

        //construct components
        ctf = new JButton("Celcius to Fahrenheit");
        ftc = new JButton("Fahrenheit to Celcius");
        lyd = new JButton("Leap Year Detector");

        //adjust size and set layout
        container.setPreferredSize(new Dimension (234, 244));
        container.setLayout(null);

        //add components
        container.add(ctf);
        container.add(ftc);
        container.add(lyd);

        //set component bounds (only needed by Absolute Positioning)
        ctf.setBounds(25, 50, 175, 25);
        ftc.setBounds(25, 105, 175, 25);
        lyd.setBounds(25, 165, 175, 25);

        frame.pack();
        frame.setVisible (true);
    }

    static void setupListeners() {
        ctf.addActionListener(listener -> celToFah());
        ftc.addActionListener(listener -> fahToCel());
        lyd.addActionListener(listener -> leapYearDetector());
    }

    static void leapYearDetector() {
        long year = Long.parseLong(JOptionPane.showInputDialog("Enter a year"));
        JOptionPane.showMessageDialog(null, "The year " + year + " was" + (isLeapYear(year) ? " " : " not ") + "a leap year");
    }

    static void fahToCel() {
        float fah = Float.parseFloat(JOptionPane.showInputDialog("Enter a temperature in Fahrenheit"));
        JOptionPane.showMessageDialog(null, "The temperature " + fah + " in Celcius is " + fToC(fah));
    }

    static void celToFah() {
        float cel = Float.parseFloat(JOptionPane.showInputDialog("Enter a temperature in Celcius"));
        JOptionPane.showMessageDialog(null, "The temperature " + cel + " in Fahrenheit is " + cToF(cel));
    }

    static boolean isLeapYear(long year) {
        return year % 4 == 0 && (year % 100 != 0 || year % 400 == 0);
    }

    static float cToF(float c) {
        String result = ""+(c * 1.8 + 32);
     //   String[] tmp = ;
  //      System.out.println(result.substring(0, result.indexOf(".")+4));
     //   result = tmp[1].length() > 3 ? tmp[1].substring(0, 3) : tmp[1];
        return Float.parseFloat(result);
    }

    static float fToC(float f) {
        String result = ""+(f - 32) / 1.8;
        return Float.parseFloat(result);
  //     return Double.parseDouble(result.length() > 5 ? result.substring(0, 5) : result);
    }
}