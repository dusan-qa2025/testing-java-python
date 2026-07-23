package org.example;
import io.cucumber.junit.CucumberOptions;
import org.junit.runner.RunWith;
import io.cucumber.junit.Cucumber;

@RunWith(Cucumber.class)
@CucumberOptions(
        features="src/test/resources/features",
        plugin={"pretty"},
        publish=true,
        glue="org.example"
)
public class TestRunner {

}
