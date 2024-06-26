import java.rmi.Naming;
import java.rmi.Remote;
import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.io.Serializable;

public class TW10Server{
    // Named inner class that implements Serializable
    static class HelloServiceImpl implements TW10Interface, Serializable {
        @Override
        public String sayHello() throws RemoteException {
            return "Hello from the server!";
        }
    }

    public static void main(String[] args) {
        try {
            // Using the named serializable inner class
            TW10Interface helloObj = new HelloServiceImpl();

            // Create and export the RMI registry on port 1099
            LocateRegistry.createRegistry(1098);

            // Bind the remote object to the registry with the name "HelloService"
            Naming.rebind("HelloService", (Remote) helloObj);

            System.out.println("Server is ready.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}