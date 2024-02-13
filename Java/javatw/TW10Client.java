import java.rmi.Naming;

public class TW10Client {
    public static void main(String[] args) {
        try {
            // Lookup the remote object with the name "HelloService"
            TW10Interface helloObj = (TW10Interface) Naming.lookup("rmi://localhost:1099/HelloService");

            // Invoke the remote method and print the result
            String result = helloObj.sayHello();
            System.out.println(result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}