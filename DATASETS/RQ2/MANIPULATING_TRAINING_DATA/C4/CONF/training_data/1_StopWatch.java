





public class StopWatch {

    
    private long startTime;
    private long endTime;

    public long getStartTime() {
        return startTime;
    }

    public long getEndTime() {
        return endTime;
    }

    
    public StopWatch() {
        startTime = System.currentTimeMillis();
    }

    
    void start() {
        startTime = System.currentTimeMillis();
    }

    
    void stop() {
        endTime = System.currentTimeMillis();
    }

    
    public long getElapsedTime() {
        return (endTime - startTime);
    }


}
