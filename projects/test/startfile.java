package fr.gonpvp.startfile;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class startfile implements Listener {

    @EventHandler 
    public void OnPlayerJoin5(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName() + "testsetseest");
    }

}
