import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
public class TW10Implementation extends UnicastRemoteObject implements 
TW10Interface {
 public TW10Implementation() throws RemoteException {
 super();
 }
 
 @Override
 public String sayHello() throws RemoteException {
 return "Hello, from the server!";
 }
 
}