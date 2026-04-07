import java.util.Scanner;

class SharedVar {
    static int value = 0;
    static final Object lock = new Object(); // for version 2
}

class IncrementThread extends Thread {
    public void run() {
        Scanner sc = new Scanner(System.in);
        System.out.print("Increment thread: Enter amount: ");
        int amt = sc.nextInt();
        //SharedVar.value += amt;   // version 1 (race)
        synchronized(SharedVar.lock) { SharedVar.value += amt; } // version 2
    }
}

class DecrementThread extends Thread {
    public void run() {
        int fixed = 5;
        //SharedVar.value -= fixed;   // version 1
        synchronized(SharedVar.lock) { SharedVar.value -= fixed; } // version 2
    }
}

class Five {
    public static void main(String[] args) throws Exception {
        System.out.println("Race condition ");
        for (int run = 1; run <= 5; run++) {
            SharedVar.value = 0;
            Thread i1 = new IncrementThread();
            Thread i2 = new IncrementThread();
            Thread d1 = new DecrementThread();
            Thread d2 = new DecrementThread();
            i1.start(); i2.start(); d1.start(); d2.start();
            i1.join(); i2.join(); d1.join(); d2.join();
            System.out.println("Run " + run + " → Final value = " + SharedVar.value);
        }

        System.out.println("\nMutual exclusion");
        // Just uncomment the synchronized blocks in the two thread classes above.
    }
}