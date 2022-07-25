import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.function.Predicate;
import java.util.function.Function;

class Filter {
    public static Predicate<String> nameStartingWithPrefix(String prefix) {
        return name -> name.startsWith(prefix);
    }
}

class Mapper {
    private static Integer count(String name) {
        Set set = new HashSet<>();
        for(int i = 0; i < name.length(); i++) {
            set.add(name.charAt(i));
        }
        return set.size();
    }
    public static Function<String, CharactersCount> getDistinctCharactersCount() {
        return name -> new CharactersCount(name, count(name));
    }
}
class CharactersCount {
    private final String name;
    private final Integer distinctCharacterCount;
    
    public CharactersCount(String name, Integer distinctCharacterCount) {
        this.name = name;
        this.distinctCharacterCount = distinctCharacterCount;
    }
    
    @Override
    public String toString() {
        return "\"" + this.name + "\" has " + this.distinctCharacterCount + " distinct characters.";
    }
}

public class Solution {
    private static final Scanner scanner = new Scanner(System.in);
    
    public static void main(String[] args) {
        List<String> names = Arrays.asList(
                "aaryanna",
                "aayanna",
                "airianna",
                "alassandra",
                "allanna",
                "allannah",
                "allessandra",
                "allianna",
                "allyanna",
                "anastaisa",
                "anastashia",
                "anastasia",
                "annabella",
                "annabelle",
                "annebelle"
        );
        
        names.stream()
                .filter(Filter.nameStartingWithPrefix(scanner.nextLine()))
                .map(Mapper.getDistinctCharactersCount())
                .forEachOrdered(System.out::println);
    }
}


