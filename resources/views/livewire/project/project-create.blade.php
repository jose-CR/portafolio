<div class="flex items-center justify-center p-6">
    <div class="w-full max-w-2xl bg-white p-8 rounded-lg shadow-md">
        <h2 class="text-2xl font-semibold text-gray-800 mb-6 text-center">New Project</h2>

        @if (session()->has('message'))
            <div class="mb-4 p-3 bg-green-200 text-green-800 rounded">
                {{ session('message') }}
            </div>
        @endif

        <form wire:submit.prevent="saveProject">
            <!-- Grid Layout -->
            <div class="grid grid-cols-2 gap-6">
                <!-- Project Name -->
                <div>
                    <label for="project_name" class="mb-2 block text-base font-medium text-gray-700">
                        Project Name
                    </label>
                    <input 
                        type="text" 
                        id="project_name"
                        wire:model="project_name"
                        placeholder="Enter project name"
                        class="w-full rounded-md border border-gray-300 bg-white py-3 px-4 text-base text-gray-700 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                    />
                    @error('project_name') <span class="text-red-500 text-sm">{{ $message }}</span> @enderror
                </div>

                <!-- Image Upload -->
                <div>
                    <label for="image" class="mb-2 block text-base font-medium text-gray-700">
                        Upload Image
                    </label>
                    <input 
                        type="file" 
                        id="image"
                        wire:model="image_url"
                        class="w-full border border-gray-300 rounded-md py-2 px-3 text-gray-700 bg-white outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                        accept="image/*"
                    />
                    @error('image_url') <span class="text-red-500 text-sm">{{ $message }}</span> @enderror

                    <!-- Mostrar vista previa de la imagen -->
                    @if ($image_url)
                        <div class="mt-4">
                            <img src="{{ $image_url->temporaryUrl() }}" class="w-full h-40 object-cover rounded-md shadow-md">
                        </div>
                    @endif
                </div>

                <!-- Project Description (Full Width) -->
                <div class="col-span-2">
                    <label for="project_description" class="mb-2 block text-base font-medium text-gray-700">
                        Project Description
                    </label>
                    <textarea 
                        rows="4"
                        id="project_description"
                        wire:model="project_description"
                        placeholder="Enter project description"
                        class="w-full resize-none rounded-md border border-gray-300 bg-white py-3 px-4 text-base text-gray-700 outline-none focus:border-indigo-500 focus:ring-1 focus:ring-indigo-500"
                    ></textarea>
                    @error('project_description') <span class="text-red-500 text-sm">{{ $message }}</span> @enderror
                </div>
            </div>

            <!-- Submit Button -->
            <div class="mt-6">
                <button 
                    type="submit"
                    class="w-full rounded-md bg-indigo-600 py-3 px-6 text-base font-semibold text-white transition duration-300 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:ring-offset-2"
                >
                    Save Project
                </button>
            </div>
        </form>
    </div>
</div>
