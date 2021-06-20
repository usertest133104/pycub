package fr.gonpvp;

import fr.gonpvp.listeners.LConnections;
import org.bukkit.plugin.java.JavaPlugin;

public final class fiffa extends JavaPlugin {

    private static fiffa INSTANCE;


    @Override
    public void onEnable() {
        INSTANCE = this;
        // Plugin startup logic
        getServer().getPluginManager().registerEvents(new LConnections(), this);

    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }

    public fiffa getInstance(){
        return INSTANCE;
    }

}
