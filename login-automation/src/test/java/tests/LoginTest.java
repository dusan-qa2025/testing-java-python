package tests;

import com.dusan.BaseTest;
import com.dusan.LoginPage;
import org.testng.Assert;
import org.testng.annotations.Test;

public class LoginTest extends BaseTest {

    @Test
    public void invalidLoginShouldShowError() {
        LoginPage loginPage = new LoginPage(driver);

        loginPage.open();
        loginPage.login("wrongUser", "wrongPass");

        Assert.assertTrue(
                loginPage.getErrorMessage().contains("Your username is invalid"),
                "Error message is NOT displayed"
        );
    }
}
