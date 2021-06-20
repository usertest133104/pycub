package exemple.author;

exemple.author.listeners.Main;
exemple.author.listeners.test;
org.bukkit.plugin.java.JavaPlugin;

public final class test extends JavaPlugin {

    private static test INSTANCE;

    @Override
    public void onEnable() {
        INSTANCE = this;
        // Plugin startup logic
        getServer().getPluginManager().registerEvents(new MaintestListener(), this);
        getServer().getPluginManager().registerEvents(new testtestListener(), this);
    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }

    public test getInstance(){
        return INSTANCE;
    }
}