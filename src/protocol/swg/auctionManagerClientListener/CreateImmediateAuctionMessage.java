/*******************************************************************************
 * Copyright (c) 2013 <Project SWG>
 * 
 * This File is part of NGECore2.
 * 
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 * Using NGEngine to work with NGECore2 is making a combined work based on NGEngine. 
 * Therefore all terms and conditions of the GNU Lesser General Public License cover the combination.
 ******************************************************************************/
package protocol.swg.auctionManagerClientListener;

import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

import org.apache.mina.core.buffer.IoBuffer;

import protocol.swg.SWGMessage;

public class CreateImmediateAuctionMessage extends SWGMessage {

	private long objectId;
	private long vendorId;
	private int price;
	private int duration;
	private String description;
	private boolean isPremium;

	@Override
	public void deserialize(IoBuffer data) {
		data.skip(6);
		this.objectId = data.getLong();
		this.vendorId = data.getLong();
		this.price = data.getInt();
		this.duration = data.getInt();
		
		int size = data.getInt();
		
		this.description = new String(ByteBuffer.allocate(size * 2).put(data.array(), data.position(), size * 2).array(), StandardCharsets.UTF_16LE);
		data.position(data.position() + size * 2);
		this.isPremium = data.get() == 0 ? false : true;
	}

	@Override
	public IoBuffer serialize() {
		// TODO Auto-generated method stub
		return null;
	}

	public long getObjectId() {
		return objectId;
	}

	public long getVendorId() {
		return vendorId;
	}

	public int getPrice() {
		return price;
	}

/*
 * @return Duration in minutes
 */
	public int getDuration() {
		return duration;
	}

	public String getDescription() {
		return description;
	}

	public boolean isPremium() {
		return isPremium;
	}

}
