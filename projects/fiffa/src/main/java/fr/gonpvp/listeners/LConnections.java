package fr.gonpvp.listeners;

import fr.gonpvp.utils.ItemBuilder;
import org.bukkit.Bukkit;
import org.bukkit.Location;
import org.bukkit.Material;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.bukkit.inventory.ItemStack;

public class LConnections implements Listener {

    @EventHandler
    public void onConnect(PlayerJoinEvent e){
        ItemStack item = new ItemBuilder(Material.TNT).setName("§aUne §ctnt §acustom").toItemStack();
        ItemStack gonitem = new ItemBuilder(Material.WOOD).setName("§cMeuble Ikéa").toItemStack();

        e.setJoinMessage(null);
        e.getPlayer().teleport(new Location(Bukkit.getWorlds().get(0), 0, 100, 0, 0, 0));
        e.getPlayer().getInventory().clear();


        e.getPlayer().getInventory().setHeldItemSlot(4);

        e.getPlayer().getInventory().setItem(4, item);
        e.getPlayer().getInventory().setItem(8, gonitem);
    }

}
