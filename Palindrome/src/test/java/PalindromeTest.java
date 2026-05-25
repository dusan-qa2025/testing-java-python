import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;


public class PalindromeTest {

    @Test
    void testSimpleWord() {
        assertTrue(Palindrome.isPalindrome("Madam"));
    }

    @Test
    void testNumberPalindrome() {
        assertTrue(Palindrome.isPalindrome("2002"));
    }

    @Test
    void testPhrasePalindrome() {
        assertTrue(Palindrome.isPalindrome("Never odd or even"));
    }

    @Test
    void testNoPalindrome() {
        assertFalse(Palindrome.isPalindrome("java"));
    }

    @Test
    void testCaseInsensitive() {
        assertTrue(Palindrome.isPalindrome("Radar"));
    }

    @Test
    void testSpecialCharacters() {
        assertTrue(Palindrome.isPalindrome("A man, a plan, a canal: Panama"));

    }
}
