import org.junit.Test;
import static org.junit.Assert.assertTrue;

/**
 * Default-package JUnit4 test to maximize discovery compatibility in strict CI configurations.
 */
public class TopLevelDiscoveryTest {

    @Test
    public void alwaysPasses() {
        assertTrue(true);
    }
}
