package fr.gonpvp.omgg;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class omgg implements Listener {

    @EventHandler 
    public void OnPlayerJoin6(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName());
    }

}
