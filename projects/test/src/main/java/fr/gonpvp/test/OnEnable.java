package gonpvp.test;

org.bukkit.plugin.java.JavaPlugin;

public final class test extends JavaPlugin {

    private static test INSTANCE;

    @Override
    public void onEnable() {
        INSTANCE = this;
        // Plugin startup logic
    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }

    public test getInstance(){
        return INSTANCE;
    }
}