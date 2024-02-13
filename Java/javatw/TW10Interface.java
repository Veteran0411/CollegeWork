import java.rmi.Remote;
import java.rmi.RemoteException;
public interface TW10Interface extends Remote {
 String sayHello() throws RemoteException;
 
}