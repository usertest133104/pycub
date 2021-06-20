package fr.gonpvp.test;

import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;

public class test implements Listener {

    @EventHandler 
    public void OnPlayerJoin2(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName());
    }


}