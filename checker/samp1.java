//package com.tutorialspoint.gui;
 
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.Scanner;
import java.io.*;
import java.math.BigInteger; 
import java.security.MessageDigest; 
import java.security.NoSuchAlgorithmException;
import javax.swing.table.DefaultTableModel;
 
public class GUI {
   private JFrame mainFrame;
   private JLabel headerLabel;
   private JLabel statusLabel;
   private JPanel controlPanel;
   private java.io.File file = new File("MD5sums");
   private int returnVal;
   private DefaultTableModel tableModel;
   private JTable table;
   private JScrollPane sp;

   public GUI(){
      prepareGUI();
   }
   public static void main(String[] args) throws IOException {
      GUI  swingControlDemo = new GUI();      
      swingControlDemo.showFileChooserDemo();
   }
   private void prepareGUI(){
      mainFrame = new JFrame("Java Swing Examples");
      mainFrame.setSize(400,600);
      mainFrame.setLayout(new GridLayout(5, 1));
      
      mainFrame.addWindowListener(new WindowAdapter() {
         public void windowClosing(WindowEvent windowEvent){
            System.exit(0);
         }        
      });    
      headerLabel = new JLabel("", JLabel.CENTER);        
      statusLabel = new JLabel("",JLabel.CENTER);    
      statusLabel.setSize(350,100);

      controlPanel = new JPanel();
      controlPanel.setLayout(new FlowLayout());

      String[] header = { "Plain-Text", "Result" };
      tableModel = new DefaultTableModel(header, 0);
      table = new JTable(tableModel);
      sp = new JScrollPane(table);

      mainFrame.add(headerLabel);
      mainFrame.add(controlPanel);
      mainFrame.add(statusLabel);
      mainFrame.add(sp);
      mainFrame.setVisible(true);  
   }

   private static String getMd5(String input) { 
    try { 

      MessageDigest md = MessageDigest.getInstance("MD5"); 
 
      byte[] messageDigest = md.digest(input.getBytes()); 
      BigInteger no = new BigInteger(1, messageDigest); 
      String hashtext = no.toString(16); 

      return hashtext; 
    }  

    catch (NoSuchAlgorithmException e) { 
      throw new RuntimeException(e); 
    } 
  }

   private void showFileChooserDemo(){
      headerLabel.setText("JFileChooser GUI for MD5 verification"); 
      final JFileChooser  fileDialog = new JFileChooser();
      JButton showFileDialogButton = new JButton("Select file");
      JButton executeProcess = new JButton("Process");

      showFileDialogButton.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e) {
            returnVal = fileDialog.showOpenDialog(mainFrame);
            
            if (returnVal == JFileChooser.APPROVE_OPTION) {
               file = fileDialog.getSelectedFile();
               statusLabel.setText("File Selected :" + file.getName());
            } else {
               statusLabel.setText("Open command cancelled by user." );           
            }      
         }
      });

      executeProcess.addActionListener(new ActionListener() {
         @Override
         public void actionPerformed(ActionEvent e2) {
            //int returnVal = fileDialog.showOpenDialog(mainFrame);
            
            //if (returnVal == JFileChooser.APPROVE_OPTION) {
               //java.io.File file = fileDialog.getSelectedFile();
                //int count = 0;
              try {
                  Scanner input = new Scanner(file);
                  while (input.hasNext()) {
                    String line = input.nextLine();
                    String[] words_array = line.split("\t");
                    //String word  = input.next();
                    //String dash = input.next();
                    //String hash_given = input.next();
                    String hash_actual = getMd5(words_array[0]);
                    if (words_array[2].equals(hash_actual)) {
                      //System.out.println(words_array[0] + ": verfied");
                      
                      tableModel.addRow(new Object[] { words_array[0], "verified" });
                    }
                    else {
                      //System.out.println(words_array[0] + ": not verified");
                      //String[] row = { word, "not verified" };
                      tableModel.addRow(new Object[] { words_array[0], "not verified" });
                    }
                    //System.out.println(word + " " + hash);
                    //count = count + 1;
                  }
                  input.close();
              }
              catch (Exception err) {
                  System.out.println(err.getClass());
              }
                    
            //}
            //else {
               //statusLabel.setText("Open command cancelled by user." );           
            //}      
         }
                
      });
      controlPanel.add(showFileDialogButton);
      controlPanel.add(executeProcess);
      mainFrame.setVisible(true);  
   }


}