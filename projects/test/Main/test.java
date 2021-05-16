package fr.gonpvp;
ent.player.PlayerJoinEvent;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
 
public class PycubEvent implements Listener {

    @EventHandler 
    public void OnPlayerJoin1(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName() + "event.getPlayer() craft" + event.getPlayer() + event.getPlayer().getName() + event.getPlayer());
    }


    @EventHandler 
    public void OnPlayerJoin2(PlayerJoinEvent event) {
        Bukkit.broadcastMessage(event.getPlayer().getName());
    }


}
