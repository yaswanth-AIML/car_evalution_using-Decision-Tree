class a extends Thread{
public void run(){
    for (int i=1;i<=10;i++){
        System.out.println("THREAD 1:"+i);
    }
}
}
class b extends Thread{
    public void run(){
        for(int i=1;i<=10;i++){
            System.out.println("THREAD 2:"+i);
        }
    }
}
public class thread_class {
    public static void main(String[]args){
    a a1=new a();
    b b1=new b();
    a1.start();
    b1.start();
}
}
