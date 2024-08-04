import java.util.Scanner;

public class Test_4 {
    public static void main(String[] args) {
        System.out.println("""
                Escolha a sua opção:
                [ 1 ] SOMAR::
                [ 2 ] SUBTRAIR::
                [ 3 ] MULTIPLICAR::
                [ 4 ] DIVIDIR::""");
        Scanner teclado = new Scanner(System.in);
        System.out.print("Escolha a sua opção: ");
        int opc = teclado.nextInt();
        if (opc == 1) {
            Somar();
        }
        else if (opc == 2) {
            Sub();
        }
        else if (opc == 3) {
            multi();
        }
        else if (opc == 4) {
            Div();
        }
        else {
            System.out.println("Essa opção não existe hahahahahahahahah");
        }
    }
    static void Somar() {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o primeiro número: ");
        int n1 = teclado.nextInt();
        System.out.print("Digite o segundo número: ");
        int n2 = teclado.nextInt();
        int soma = n1 + n2;
        System.out.printf("A soma entre %d e %d é: %d", n1, n2, soma);
    }
    static void Sub() {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o primeiro número: ");
        int n1 = teclado.nextInt();
        System.out.print("Digite o segundo número: ");
        int n2 = teclado.nextInt();
        int sub = n1 - n2;
        System.out.printf("A subtração entre %d e %d é: %d", n1, n2, sub);
    }
    static void Div() {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o primeiro número: ");
        int n1 = teclado.nextInt();
        System.out.print("Digite o segundo número: ");
        int n2 = teclado.nextInt();
        float div = (float) n1 / n2;
        System.out.printf("A divisão entre %d e %d é: %.2f", n1, n2, div);
    }
    static void multi() {
        Scanner teclado = new Scanner(System.in);
        System.out.print("Digite o primeiro número: ");
        int n1 = teclado.nextInt();
        System.out.print("Digite o segundo número: ");
        int n2 = teclado.nextInt();
        float multi = (float) n1 * n2;
        System.out.printf("A multiplicação entre %d e %d é: %.2f", n1, n2, multi);
    }
}
