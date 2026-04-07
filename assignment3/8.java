class NoticeBoard {
    private String content = "Initial notice";
    private int readers = 0;
    private boolean writing = false;

    public synchronized void startRead() throws InterruptedException {
        while (writing) {
            System.out.println(Thread.currentThread().getName() + " is waiting for the update to finish.");
            wait();
        }
        readers++;
    }

    public synchronized void endRead() {
        readers--;
        if (readers == 0) notifyAll();
    }

    public synchronized void startWrite() throws InterruptedException {
        while (readers > 0 || writing) {
            System.out.println(Thread.currentThread().getName() + " is waiting for the update to finish.");
            wait();
        }
        writing = true;
    }

    public synchronized void endWrite() {
        writing = false;
        notifyAll();
    }

    public String read() { return content; }
    public void write(String newContent) { content = newContent; }
}

class Eight {
    public static void main(String[] args) throws InterruptedException {
        NoticeBoard board = new NoticeBoard();

        // Multiple readers
        for (int i = 1; i <= 3; i++) {
            new Thread(() -> {
                try {
                    board.startRead();
                    System.out.println(Thread.currentThread().getName() + " reads: " + board.read());
                    Thread.sleep(100);
                    board.endRead();
                } catch (Exception ignored) {}
            }, "Reader-" + i).start();
        }

        // Writers
        new Thread(() -> {
            try {
                board.startWrite();
                board.write("New notice: Exam on 15th April");
                System.out.println(Thread.currentThread().getName() + " wrote new notice");
                board.endWrite();
            } catch (Exception ignored) {}
        }, "Writer-1").start();

        new Thread(() -> {
            try {
                board.startWrite();
                board.write("Updated: Assignment 3 due tomorrow");
                System.out.println(Thread.currentThread().getName() + " wrote new notice");
                board.endWrite();
            } catch (Exception ignored) {}
        }, "Writer-2").start();
    }
}