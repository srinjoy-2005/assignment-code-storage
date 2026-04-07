import java.util.function.IntConsumer;

class FizzBuzz {
    private int n;
    private int current = 1;

    public FizzBuzz(int n) { this.n = n; }

    public synchronized void fizz(Runnable printFizz) throws InterruptedException {
        while (current <= n) {
            if (current % 3 == 0 && current % 5 != 0) {
                printFizz.run();
                current++;
                notifyAll();
            } else wait();
        }
    }

    public synchronized void buzz(Runnable printBuzz) throws InterruptedException {
        while (current <= n) {
            if (current % 5 == 0 && current % 3 != 0) {
                printBuzz.run();
                current++;
                notifyAll();
            } else wait();
        }
    }

    public synchronized void fizzbuzz(Runnable printFizzBuzz) throws InterruptedException {
        while (current <= n) {
            if (current % 15 == 0) {
                printFizzBuzz.run();
                current++;
                notifyAll();
            } else wait();
        }
    }

    public synchronized void number(IntConsumer printNumber) throws InterruptedException {
        while (current <= n) {
            if (current % 3 != 0 && current % 5 != 0) {
                printNumber.accept(current);
                current++;
                notifyAll();
            } else wait();
        }
    }
}

class Six {
    public static void main(String[] args) throws InterruptedException {
        FizzBuzz fb = new FizzBuzz(15);
        Thread A = new Thread(() -> { try { fb.fizz(() -> System.out.print("fizz ")); } catch (Exception ignored) {} });
        Thread B = new Thread(() -> { try { fb.buzz(() -> System.out.print("buzz ")); } catch (Exception ignored) {} });
        Thread C = new Thread(() -> { try { fb.fizzbuzz(() -> System.out.print("fizzbuzz ")); } catch (Exception ignored) {} });
        Thread D = new Thread(() -> { try { fb.number(x -> System.out.print(x + " ")); } catch (Exception ignored) {} });

        A.start(); B.start(); C.start(); D.start();
        // Repeat runs to see non-determinism if synchronization is removed
    }
}