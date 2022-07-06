import java.util.Arrays;

public class JavaCodeUsingArray {

    public static void main(String[] args) {
        int[] arr = {1,0,2,3,0,4,5,0};
        System.out.println(Arrays.toString(duplicateZeros(arr)));
    }

    public static int[] duplicateZeros(int[] arr) {

        int[] temp = new int [arr.length];
		int j = 0;

		for (int i = 0 ; i < arr.length - j; i++) {
			temp[i + j] = arr[i]; 
			if (arr[i] == 0) {                        
				j++; 
				temp[i+j] = arr[i]; 
			}
		}

		for (int i = 0; i < arr.length; i++) {
			arr[i] = temp[i];   
		}

        return arr;
    }
}
