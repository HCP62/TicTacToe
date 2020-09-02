/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package TicTacToe;
import java.util.*;
/**
 *
 * @author ameya
 */
public class TicTacToe {
    public static String[][] board;
    public static void main(String[] args) {
        playGame();
    }
    
    private static void initGrid(){
    board = new String[3][3];
    // fill with ~
    for (int i = 0; i < board.length; i++){
        for (int j = 0; j < board[i].length; j++){
            board[i][j] = "[ ]";
        }
    }
    }
    
    private static void printGrid(){
        System.out.println("TicTacToe Board");   
        for (int i = 0; i < board.length; i++){
            String row = "";
            for(int j = 0; j < board[i].length; j++){
                row += (board[i][j] + " ");
            }
            System.out.println(row);
        } 
        System.out.println("");        
    }
    
    public static boolean threeInARow(String val){
        //top row
        if ((board[0][0].equals(board[0][1]) && board[0][2].equals(board[0][0])) && board[0][0].equals(val)){
            return true;
        }
        // middle row
        if ((board[1][0].equals(board[1][1]) && board[1][2].equals(board[1][0])) && board[1][0].equals(val)){
            return true;
        }
        // bottom row
        if ((board[2][0].equals(board[2][1]) && board[2][2].equals(board[2][0])) && board[2][0].equals(val)){
            return true;
        }
        //diagonals
        if ((board[0][0].equals(board[2][2]) && board[0][0].equals(board[1][1]) && board[0][0].equals(val))){
            return true;
        }
        if ((board[2][0].equals(board[1][1]) && board[1][1].equals(board[0][2])) && board[1][1].equals(val)){
            return true;
        }
        if ((board[0][0].equals(board[1][0]) && board[1][0].equals(board[2][0])) && board[1][0].equals(val)){
            return true;
        }
        if ((board[2][1].equals(board[1][1]) && board[1][1].equals(board[0][1])) && board[1][1].equals(val)){
            return true;
        }
        if ((board[2][2].equals(board[1][2]) && board[1][2].equals(board[0][2])) && board[1][2].equals(val)){
            return true;
        }
        
        return false;
    }
    
    public static boolean findDraw(){
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                if (board[i][j].equals("[ ]")){
                    return false;
                }
            }
        }
        return true;
    }
    
    public static boolean playerChooses(){
        Scanner in = new Scanner(System.in);
        while (true){
            System.out.println("Choose a row (0-2): ");
            int r = in.nextInt();
            System.out.println("Choose a column (0-2): ");
            int c = in.nextInt();
            if (r < 0 || r > 2 || c < 0 || c > 2){
                continue;
            }
            if (board[r][c].equals("[ ]")){
                board[r][c] = "[X]";
                break;
            }
        }
        printGrid();
        System.out.println(" ");
        if (threeInARow("[X]")){
            System.out.println("Congrats you win!");
            return true;
        }
        else if (findDraw()){
        System.out.println("DRAW");
        return true;
        }
        else{
            return false;
        }
    }
    
    public static void computerChoosesRand(String val){
        Random rand = new Random();
        while (true){
            int compR = rand.nextInt(2);
            int compC = rand.nextInt(2);
            if (board[compR][compC].equals("[ ]")){
                board[compR][compC] = val;
                break;
            }
        }
    }
    
    public static int makeScore(int depth, String comp, String player){
        if (threeInARow(comp)){
            return 1;
        }
        if (threeInARow(player)){
            return -1;
        }
        
        return 0;
    }
    
    public static int[] minimaxRecursive(int depth, String comp, String player, int val){
        int score;
        int[] best;
        if (val == 1){
            best = new int[]{-1,-1, Integer.MIN_VALUE};
        }
        else{
            best = new int[]{-1,-1, Integer.MAX_VALUE};
        }
        
        if(depth == 0 || threeInARow(comp) || threeInARow(player)){
            score = makeScore(depth, comp, player);
            int[] finishedGame = new int[]{-1,-1,score};
            return finishedGame;
        }
        
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                if (board[i][j].equals("[ ]")){
                    if (val == 1){
                        board[i][j] = comp;
                    }
                    else{
                        board[i][j] = player;
                    }
                    int[] copyScore = minimaxRecursive(depth-1, comp, player, -1*val);
                    board[i][j] = "[ ]";
                    copyScore[0] = i;
                    copyScore[1] = j;
                    
                    if (val == 1 && copyScore[2] > best[2]){
                        best = copyScore;
                    }
                    else if (val != 1 && copyScore[2] < best[2]){
                        best = copyScore;
                    }
                }
            }
        }
        
        return best;
    }
    
    public static void minimaxAI(String val, String player){
        int filled = 0;
        for (int i = 0; i < board.length; i++){
            for (int j = 0; j < board[i].length; j++){
                if (!(board[i][j].equals("[ ]"))){
                    filled++;
                }
            }
        }
        if (9-filled == 0 || threeInARow(val) || threeInARow(player)){
            return;
        }
        if (filled == 0){
            computerChoosesRand(val);
            return;
        }
        int[] score = minimaxRecursive(9-filled, val, player, 1);
        if (score[0] < 0 || score[1] < 0){
            computerChoosesRand(val);
        }
        else{
            board[score[0]][score[1]] = val;
        }
    }
    
    public static void playGame(){
        initGrid();
        String player = "[X]";
        String computer = "[O]";
        
        while(true){
            printGrid();
            System.out.println(" ");
            if (threeInARow(computer)){
                System.out.println("YOU LOSE");
            }
            else if (findDraw()){
                System.out.println("DRAW");
            }
            
            if (playerChooses()){
                break;
            }
            minimaxAI(computer, player);
        }
    }
}
