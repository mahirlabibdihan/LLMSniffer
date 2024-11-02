

import java.util.Random;
import java.util.Scanner;

public class Adult {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (true) {
            System.out.println("[주민등록번호 계산]");
            System.out.print("출생년도를 입력해 주세요.(yyyy) : ");
            int year = sc.nextInt();
            if (year < 1000 || year > 2023) {
                System.out.println("출생년도 4자리를 정확히 입력해 주세요.");
                System.out.println("입력 값이 초기화 되었습니다.");
                System.out.println();
                continue;
            }
            System.out.print("출생월을 입력해 주세요.(mm) : ");
            int month = sc.nextInt();
            if (month <= 0 || month > 12) {
                System.out.println("출생월(0~12)을 정확히 입력해 주세요.");
                System.out.println("입력 값이 초기화 되었습니다.");
                System.out.println();
                continue;
            }
            System.out.print("출생일을 입력해 주세요.(dd) : ");
            int day = sc.nextInt();
            if (day <= 0 || day > 31) {
                System.out.println("출생일(1~31)을 정확히 입력해 주세요.");
                System.out.println("입력 값이 초기화 되었습니다.");
                System.out.println();
                continue;
            }
            int num1 = 0;
            System.out.print("성별을 입력해 주세요.(m/f) : ");
            char gender = sc.next().charAt(0);

            if (gender == 'm' && year < 2000) {
                num1 = 1;
            } else if (gender == 'f' && year < 2000) {
                num1 = 2;
            } else if (gender == 'm' && year >= 2000) {
                num1 = 3;
            } else if (gender == 'f' && year >= 2000) {
                num1 = 4;
            } else {
                System.out.println("성별(m/f)을 정확히 입력해주세요.");
                System.out.println("입력 값이 초기화 되었습니다.");
                System.out.println();
                continue;
            }

            System.out.print(String.format("%d%02d%02d" + "-" + "%d", year, month, day, num1));

            Random random = new Random();
            for (int i = 0; i < 6; i++) {
                System.out.print(random.nextInt(10));
            }
            break;
        }
    }
}