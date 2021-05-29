package fr.gonpvp.main;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class Main implements Listener {

    @EventHandler 
    public void OnPlayerJoin1(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName() + "testsetseest");
        Bukkit.broadcastMessage(event.getPlayer().getName() + "testsetseest");
    }


}